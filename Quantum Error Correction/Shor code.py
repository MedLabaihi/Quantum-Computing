import os
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq import least_busy
from qiskit.ignis.mitigation.measurement import complete_meas_cal, CompleteMeasFitter

def initialize_ibmq(api_key=None):
    """Initialize IBMQ account and get provider."""
    if api_key:
        IBMQ.enable_account(api_key)
    elif os.getenv('IBMQ_API_KEY'):
        IBMQ.enable_account(os.getenv('IBMQ_API_KEY'))
    else:
        raise ValueError("API Key not provided. Set the 'IBMQ_API_KEY' environment variable or pass it directly.")
    provider = IBMQ.get_provider(hub='ibm-q')
    return provider

def calibrate_measurement(backend):
    """Perform measurement error mitigation calibration."""
    qr_cal = QuantumRegister(9)
    cr_cal = ClassicalRegister(9)
    meas_calib_circuits, state_labels = complete_meas_cal(qr=qr_cal, cr=cr_cal)
    cal_job = execute(meas_calib_circuits, backend=backend, shots=1000)
    cal_results = cal_job.result()
    meas_fitter = CompleteMeasFitter(cal_results, state_labels)
    return meas_fitter

def create_shor_circuit():
    """Create and return a Shor code quantum circuit."""
    q = QuantumRegister(9, 'q')
    c = ClassicalRegister(1, 'c')
    circuit = QuantumCircuit(q, c)

    # Encoding
    circuit.cx(q[0], q[3])
    circuit.cx(q[0], q[6])
    circuit.h(q[0])
    circuit.h(q[3])
    circuit.h(q[6])
    circuit.cx(q[0], q[1])
    circuit.cx(q[3], q[4])
    circuit.cx(q[6], q[7])
    circuit.cx(q[0], q[2])
    circuit.cx(q[3], q[5])
    circuit.cx(q[6], q[8])
    circuit.barrier(q)

    # Introduce Errors
    circuit.x(q[0])  # Bit flip error
    circuit.z(q[0])  # Phase flip error
    circuit.barrier(q)

    # Error Correction
    circuit.cx(q[0], q[1])
    circuit.cx(q[3], q[4])
    circuit.cx(q[6], q[7])
    circuit.cx(q[0], q[2])
    circuit.cx(q[3], q[5])
    circuit.cx(q[6], q[8])
    circuit.ccx(q[1], q[2], q[0])
    circuit.ccx(q[4], q[5], q[3])
    circuit.ccx(q[7], q[8], q[6])
    circuit.h(q[0])
    circuit.h(q[3])
    circuit.h(q[6])
    circuit.cx(q[0], q[3])
    circuit.cx(q[0], q[6])
    circuit.ccx(q[3], q[6], q[0])
    circuit.barrier(q)

    # Measurement
    circuit.measure(q[0], c[0])
    return circuit

def execute_circuit(circuit, backend):
    """Execute the quantum circuit and return the result counts."""
    job = execute(circuit, backend=backend, shots=1000)
    job_monitor(job)
    result = job.result()
    counts = result.get_counts()
    return counts

def main():
    print('\nShor Code')
    print('--------------')

    # Initialize IBMQ and get backend
    provider = initialize_ibmq('ENTER API KEY HERE')
    backend = least_busy(provider.backends(filters=lambda x: x.configuration().simulator and x.status().operational))

    # Perform measurement error mitigation calibration
    meas_fitter = calibrate_measurement(backend)

    # Create and execute Shor code circuit
    circuit = create_shor_circuit()
    counts = execute_circuit(circuit, backend)

    # Apply measurement error mitigation
    meas_fitter_results = meas_fitter.filter.apply(counts)

    print("\nShor code with bit flip and phase error (with error mitigation)")
    print("----------------------------------------------------------------")
    print(meas_fitter_results)

    # Optional: Draw the circuit
    circuit.draw(output='mpl', filename='shorcode_optimized.png')

if __name__ == "__main__":
    main()
