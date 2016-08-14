var first_variable = "Yipee I was first!";
console.log(first_variable);
function firstFunc() {
  console.log(first_variable)
}
first_variable = "Not anymore!!!";
console.log(first_variable);


var food = "gone"
function eat() {
  var food = "Chicken";
  console.log(food);
  food = "half-chicken";
  console.log(food);
}
eat();
console.log(food);

new_word = "old";
function lastFunc() {
  var new_word = "NEW!";
  console.log(new_word);
}
lastFunc()
