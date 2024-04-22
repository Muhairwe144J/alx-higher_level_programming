// Since myVar is const in 100-main.js, we cannot modify it directly.
// However, we can create a new object with the desired value.

const modifiedObject = {
  value: 333 // Set the new value here
};

console.log('myVar from 100-let_me_const.js:', modifiedObject.value); // Access the value from the new object
