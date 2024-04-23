// Sample JSON data
var jsonData = '[{"name":"John","age":30},{"name":"Jane","age":25},{"name":"Tom","age":40}]';

// Parse JSON data into a JavaScript object
var data = JSON.parse(jsonData);

// Create an empty array to store table rows
var tableData = [];

// Iterate over the data and extract information for table rows
data.forEach(function(item) {
    var row = []; // Create an empty array for each row
    row.push(item.name); // Push name into the row array
    row.push(item.age); // Push age into the row array
    tableData.push(row); // Push the row array into the tableData array
});

// Now you have tableData array populated with data from JSON

// Now you can populate your HTML table dynamically
var table = document.getElementById('myTable'); // Assuming your table has an ID 'myTable'

// Loop through the tableData array and populate the HTML table
tableData.forEach(function(rowData) {
    var row = table.insertRow(); // Insert a new row into the table
    rowData.forEach(function(cellData) {
        var cell = row.insertCell(); // Insert a new cell into the row
        cell.appendChild(document.createTextNode(cellData)); // Add text node with cellData to the cell
    });
});
