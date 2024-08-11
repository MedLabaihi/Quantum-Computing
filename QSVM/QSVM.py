import numpy as np
from qiskit import IBMQ, Aer
from qiskit.algorithms import QSVM
from qiskit.circuit.library import ZZFeatureMap
from qiskit.utils import QuantumInstance
from qiskit.circuit.library import SecondOrderExpansion

# Constants
SHOTS = 8192  # Number of times the job will be run on the quantum device

# Training and testing data
training_data = {
    'A': np.asarray([[0.324], [0.565], [0.231], [0.756], [0.324], [0.534], [0.132], [0.344]]),
    'B': np.asarray([[1.324], [1.565], [1.231], [1.756], [1.324], [1.534], [1.132], [1.344]])
}
testing_data = {
    'A': np.asarray([[0.024], [0.456], [0.065], [0.044], [0.324]]),
    'B': np.asarray([[1.777], [1.341], [1.514], [1.204], [1.135]])
}

def main():
    try:
        # Initialize IBMQ account
        IBMQ.load_account()
        provider = IBMQ.get_provider(hub='ibm-q')

        # Select backend
        backend = provider.get_backend('ibmq_qasm_simulator')

        # Define feature map
        num_qubits = 1
        feature_map = SecondOrderExpansion(feature_dimension=num_qubits, depth=2, entanglement='full')

        # Initialize QSVM
        svm = QSVM(feature_map, training_data, testing_data)

        # Set up quantum instance
        quantum_instance = QuantumInstance(backend, shots=SHOTS, skip_qobj_validation=False)

        print('Running....\n')

        # Run QSVM and get results
        result = svm.run(quantum_instance)

        # Data for prediction
        data = np.array([[1.453], [1.023], [0.135], [0.266]])

        # Predict using QSVM
        prediction = svm.predict(data, quantum_instance)

        # Output results
        print('Prediction of Smoker or Non-Smoker based upon gene expression of CDKN2A\n')
        print('Accuracy: ', result['testing_accuracy'], '\n')
        print('Prediction from input data where 0 = Non-Smoker and 1 = Smoker\n')
        print(prediction)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
