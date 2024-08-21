
fetch('marks.json').then((response) => response.json()).then((data) => {
}).catch((error) => console.log('error'));


function calculateCGPA() {
var grades = [];
for (var i = 1; i <= 23; i++) {
    grades.push(parseInt(document.getElementById('course' + i).value));
}
for (var i = 1; i <= 13; i++) {
    grades.push(parseInt(document.getElementById('lab' + i).value));
}

var credits = [3, 3, 4, 3, 3, 3, 2, 2, 2, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 3, 4, 3, 3, 3];

var totalCredits = 98;
var totalGradePoints = 0;

for (var i = 0; i < grades.length; i++) {
    totalGradePoints += grades[i] * credits[i];
}

var cgpa = totalGradePoints / totalCredits;
document.getElementById("result").innerText = "Your CGPA is: " + cgpa.toFixed(2);
}
