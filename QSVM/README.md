# QSVM Implementation with Qiskit

## Table of Contents
1. [Overview](#overview)
2. [Mathematical Background](#mathematical-background)
   - [Support Vector Machines (SVM)](#support-vector-machines-svm)
   - [Quantum Computing](#quantum-computing)
   - [Quantum Feature Maps](#quantum-feature-maps)
   - [Quantum SVM (QSVM)](#quantum-svm-qsqvm)
3. [Steps in the Code](#steps-in-the-code)
4. [Theoretical Advantages of QSVM](#theoretical-advantages-of-qsqvm)
5. [Complexity Analysis](#complexity-analysis)
   - [Classical SVM Complexity](#classical-svm-complexity)
   - [Quantum SVM Complexity](#quantum-svm-complexity)
6. [Practical Considerations](#practical-considerations)
7. [Summary of Complexity](#summary-of-complexity)
8. [Program Description](#program-description)
   - [Functions](#functions)
   - [Libraries](#libraries)
   - [Code Workflow](#code-workflow)
9. [Contact](#contact)

## Overview
This project demonstrates the implementation of a Quantum Support Vector Machine (QSVM) using IBM's Qiskit framework. The QSVM extends the classical SVM algorithm by leveraging quantum computing to potentially tackle classification problems that are challenging for classical methods. The implementation includes data encoding, quantum feature map construction, model training, and prediction, with an emphasis on the theoretical advantages of quantum computing.

## Mathematical Background

### Support Vector Machines (SVM)
SVM is a supervised learning algorithm used for classification. The goal is to find an optimal hyperplane that separates data points of different classes in a feature space.

- **Hyperplane:** In an $n$-dimensional space, a hyperplane is a flat affine subspace of dimension $n-1$. SVM aims to maximize the margin between classes.
- **Margin:** The distance between the hyperplane and the nearest data points from either class (support vectors). Maximizing this margin improves generalization.
- **Kernel Trick:** Enables efficient classification in higher-dimensional spaces by using kernel functions to compute the inner product in the feature space.

### Quantum Computing
Quantum computing utilizes principles of quantum mechanics to process information differently from classical computing.

- **Qubits:** Quantum bits that can exist in a superposition of states, representing both 0 and 1 simultaneously.
- **Quantum Gates:** Operations that manipulate qubits, similar to classical logic gates, described by unitary matrices.
- **Quantum Entanglement:** A phenomenon where qubits become correlated, such that the state of one affects the other, regardless of distance.
- **Quantum Measurement:** Observing qubits collapses their state to a definite 0 or 1.

### Quantum Feature Maps
In QSVM, Quantum Feature Maps encode classical data into quantum states via parameterized quantum circuits.

- **Second-Order Expansion Feature Map:** Transforms classical data $\vec{x}$ into a quantum state $\phi(\vec{x})$ using the formula:
  $$
  \phi(\vec{x}) = \exp \left( i \sum_{j < k} \gamma x_j x_k Z_j Z_k \right) \exp \left( i \sum_{j} \gamma x_j Z_j \right)
  $$
  where $\gamma$ controls data spread, and $Z_j$, $Z_k$ are Pauli-Z operators applied to qubits.

### Quantum SVM (QSVM)
QSVM replaces the classical SVM kernel with a quantum kernel, computing the inner product between quantum states in a high-dimensional Hilbert space.

- **Quantum Kernel:** The kernel function $K(\vec{x}, \vec{y})$ is computed as:
  $$
  K(\vec{x}, \vec{y}) = \left| \langle \phi(\vec{x}) | \phi(\vec{y}) \rangle \right|^2
  $$
- **Training:** Finds the optimal hyperplane in the quantum feature space by maximizing the margin between classes.
- **Prediction:** Uses the quantum kernel to classify new data.

## Steps in the Code
1. **Feature Map Construction:** Maps classical data points to quantum states using the SecondOrderExpansion feature map.
2. **QSVM Training:** Computes the quantum kernel and solves the SVM optimization problem.
3. **Testing and Prediction:** Evaluates the QSVM's performance on test data and predicts new data points.

## Theoretical Advantages of QSVM
- **Higher Dimensional Spaces:** Quantum feature maps can represent data in exponentially larger spaces, capturing complex patterns.
- **Speedup:** Potential speedup in kernel computation under certain conditions, leading to faster training and predictions.

## Complexity Analysis

### Classical SVM Complexity
- **Training Time Complexity:** Typically $O(n^2 \times d)$ to $O(n^3)$, where $n$ is the number of training samples and $d$ is the feature space dimensionality.
- **Prediction Time Complexity:** $O(n \times d)$ for a single test sample.

### Quantum SVM Complexity
- **Quantum Feature Map (Circuit Depth and Width):** 
  - **Circuit Depth:** Scales with $O(d^2)$ or higher.
  - **Circuit Width (Qubits):** Generally $O(d)$ qubits.
- **Kernel Computation:**
  - **Quantum Kernel Evaluation:** Complexity influenced by the number of shots $O(s)$.
  - **Overall Kernel Matrix Computation:** $O(n^2 \times \text{quantum kernel evaluation time})$.
- **Training Complexity:** Similar to classical SVMs but with quantum kernel overhead, typically $O(n^2)$ to $O(n^3)$.
- **Prediction Complexity:** $O(n \times \text{quantum kernel evaluation time})$ per test sample.

## Practical Considerations
- **Quantum Speedup and Bottlenecks:** QSVM may offer speedup if quantum kernel computation is faster. Bottlenecks include quantum circuit depth, shot complexity, and data loading challenges.



QSVMs have the potential to outperform classical SVMs in high-dimensional feature spaces, depending on the efficiency of quantum kernel evaluation and current quantum hardware limitations.

## Program Description

The code provided uses Qiskit to implement a Quantum Support Vector Machine (QSVM) for a binary classification problem. The code initializes a quantum feature map using the SecondOrderExpansion method, trains a QSVM on the training data, and then tests the model on the test data.

### Code Workflow
1. **Quantum Environment Setup:** The Qiskit library and necessary modules for QSVM are imported. The IBMQ provider is enabled using an API key, allowing access to IBM quantum devices.
2. **Data Preparation:**
   - The training data consists of two classes, A and B, each with several 1D data points.
   - The testing data is also prepared in the same manner.
3. **Quantum Backend Selection:** The code selects the `ibmq_qasm_simulator` backend, which simulates quantum circuits using classical resources.
4. **Feature Map Creation:** A quantum feature map is generated using the SecondOrderExpansion method. This method transforms classical data into a higher-dimensional quantum space, where the QSVM can operate.
5. **QSVM Initialization:** The QSVM is created using the quantum feature map and the training/testing data.
6. **Training and Prediction:**
   - The model is trained on the quantum backend specified earlier.
   - The trained model's accuracy is then evaluated on the test data.
   - The model is used to predict the class of new, unlabeled data points.
7. **Output:** The code prints the accuracy of the QSVM on the testing data and the predictions for the new unlabeled data.

**Example Output:**
```bash
Quantum SVM
-----------

Running....

Prediction of Smoker or Non-Smoker based upon gene expression of CDKN2A
Accuracy: 0.8 

Prediction from input data where 0 = Non-Smoker and 1 = Smoker
[1, 1, 0, 0]
```

**Points to Consider:**
- **API Key:** Replace 'ENTER API KEY HERE' with your actual IBMQ API key to access the quantum backends.
- **Quantum Backend:** You can use actual quantum hardware by replacing `ibmq_qasm_simulator` with an actual quantum backend, like `ibmq_lima`, `ibmq_quito`, etc., but this will require access to such devices and might be slower.
- **Data:** The dataset used here is small. For practical applications, larger datasets and more complex feature maps might be necessary.
- **Dependencies:** Ensure that Qiskit is installed and up to date.

This script provides a basic example of using QSVM for binary classification tasks using quantum computing principles.

## Contact
For any questions or further information, please contact.
**LABAIHI Mohammed :**
- **Email**: [m.labaihi@gmail.com](m.labaihi@gmail.com)    
- **LinkedIn**: [linkedin.com/in/labaihi](linkedin.com/in/labaihi)  
- **GitHub**: [github.com/LABAIHI_Mohammed](https://github.com/MedLabaihi)  
