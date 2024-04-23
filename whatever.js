import data from './teamdata.json';
const someTeams = [];

console.log(data[0]);
for (let i = 0; i < data.length; i++) {
    const team = {

        id: i,
        teamName: data[i].theTeamName,
        teamWins: data[i].theTeamWins,
        teamLosses: data[i].theTeamLosses,
        teamOffense: data[i].theTeamOffense,
        teamDefense: data[i].theTeamDefense,
        teamRating: data[i].theTeamRating,
        projectedWins: data[i].theProjectedWins,

        rank: i + 1,
    }
    someTeams.push(team);
}

console.log(someTeams)

function makeTableHTML(myArray) {
    var result = "<table>";
    result += "<thead>";
    result += "<tr>";
    result += "<th>Team</th>";
    result += "<th>Wins</th>";
    result += "<th>Losses</th>";
    result += "<th>Offensive Rating</th>";
    result += "<th>Defensive Rating</th>";
    result += "<th>Net Rating</th>";
    result += "<th>Projected Wins</th>";
    result += "<tr>";
    result += "</thead>";
    result += "<tbody>";

    for (var i = 0; i < myArray.length; i++) {
        result += "<tr>";
        for (var j = 0; j < myArray[i].length; j++) {
            result += "<td>" + myArray[i][j] + "</td>";
        }
        result += "</tr>";
    }
    result += "</tbody>";
    result += "</table>";

    return result;
}



