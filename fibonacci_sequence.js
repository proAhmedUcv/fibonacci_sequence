function fibonacciSequence(n) {
    if (n <= 0) {
        console.log("Please enter a positive integer.");
        return;
    }

    let sequence = [];
    let a = 0, b = 1;

    for (let i = 0; i < n; i++) {
        sequence.push(a);
        [a, b] = [b, a + b];
    }

    return sequence;
}

// Get user input
let num = parseInt(prompt("Enter a positive integer:"));

// Calculate and print the Fibonacci sequence
let result = fibonacciSequence(num);
if (result !== undefined) {
    console.log(result);
}