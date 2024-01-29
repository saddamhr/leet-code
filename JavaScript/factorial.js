const getFactorial =  (num) => {
    if (num == 0 || num == 1) return 1
    else return num * getFactorial(num - 1)
}

console.log(getFactorial(4))