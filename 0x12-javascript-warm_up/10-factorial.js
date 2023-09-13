#!/usr/bin/node
function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1); // Factorial of NaN and 0 is 1
  }
  return (n * factorial(n - 1));
}

console.log(factorial(Number(process.argv[2])));
