import os
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import plot_histogram
from qiskit.providers.ibmq import least_busy

# Function to initialize IBMQ
def initialize_ibmq():
    api_key = os.getenv('IBMQ_API_KEY')  # Use environment variable for API key
    if api_key:
        IBMQ.enable_account(api_key)
    else:
        raise ValueError("API Key not found. Set the 'IBMQ_API_KEY' environment variable.")
    provider = IBMQ.get_provider(hub='ibm-q')
    return provider

# Function to create the quantum circuit
def create_circuit():
    q = QuantumRegister(3, 'q')
    c = ClassicalRegister(1, 'c')
    circuit = QuantumCircuit(q, c)

    # Encoding
    circuit.cx(q[0], q[1])
    circuit.cx(q[0], q[2])

    # Simulate a bit flip error
    circuit.x(q[0])

    # Decoding
    circuit.cx(q[0], q[1])
    circuit.cx(q[0], q[2])
    circuit.ccx(q[2], q[1], q[0])

    # Measure the first qubit
    circuit.measure(q[0], c[0])

    return circuit

# Function to execute the circuit
def execute_circuit(circuit, provider):
    backend = least_busy(provider.backends(filters=lambda x: x.configuration().simulator))
    job = execute(circuit, backend, shots=1000)
    job_monitor(job)
    result = job.result()
    counts = result.get_counts()
    return counts

# Main function
def main():
    print('\nBit Flip Code')
    print('--------------')

    provider = initialize_ibmq()
    circuit = create_circuit()
    counts = execute_circuit(circuit, provider)

    print("\nBit flip code with error")
    print("----------------------")
    print(counts)

    # Optional: Plot histogram
    plot_histogram(counts).show()

if __name__ == "__main__":
    main()
