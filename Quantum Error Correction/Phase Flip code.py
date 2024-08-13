import os
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import plot_histogram
from qiskit.providers.ibmq import least_busy

# Function to initialize IBMQ
def initialize_ibmq(api_key=None):
    if api_key:
        IBMQ.enable_account(api_key)
    elif os.getenv('IBMQ_API_KEY'):
        IBMQ.enable_account(os.getenv('IBMQ_API_KEY'))
    else:
        raise ValueError("API Key not provided. Set the 'IBMQ_API_KEY' environment variable or pass it directly.")
    provider = IBMQ.get_provider(hub='ibm-q')
    return provider

# Function to create the quantum circuit
def create_phase_flip_circuit(apply_error=True):
    q = QuantumRegister(3, 'q')
    c = ClassicalRegister(1, 'c')
    circuit = QuantumCircuit(q, c)

    # Encoding
    circuit.cx(q[0], q[1])
    circuit.cx(q[0], q[2])

    # Apply Hadamard gates
    circuit.h(q[0])
    circuit.h(q[1])
    circuit.h(q[2])

    # Simulate a phase flip error (optional)
    if apply_error:
        circuit.z(q[0])

    # Apply Hadamard gates again
    circuit.h(q[0])
    circuit.h(q[1])
    circuit.h(q[2])

    # Decoding
    circuit.cx(q[0], q[1])
    circuit.cx(q[0], q[2])
    circuit.ccx(q[2], q[1], q[0])

    # Measure the first qubit
    circuit.measure(q[0], c[0])

    return circuit

# Function to execute the circuit
def execute_circuit(circuit, provider):
    backend = least_busy(provider.backends(filters=lambda x: x.configuration().simulator and x.status().operational))
    job = execute(circuit, backend, shots=1000)
    job_monitor(job)
    result = job.result()
    counts = result.get_counts()
    return counts

# Main function
def main():
    print('\nPhase Flip Code')
    print('----------------')

    # Initialize IBMQ
    provider = initialize_ibmq('ENTER API KEY HERE')

    # Create the quantum circuit with an error
    circuit = create_phase_flip_circuit(apply_error=True)
    counts = execute_circuit(circuit, provider)

    print("\nPhase flip code with error")
    print("----------------------")
    print(counts)

    # Optional: Plot histogram
    plot_histogram(counts).show()

if __name__ == "__main__":
    main()
