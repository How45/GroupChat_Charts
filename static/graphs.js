const colours = [
    'rgb(239, 146, 132)',
    'rgb(239, 178, 132)',
    'rgb(239, 229, 132)',
    'rgb(214, 239, 132)',
    'rgb(158, 132, 239)',
    'rgb(132, 239, 160)',
    'rgb(132, 239, 219)',
    'rgb(132, 168, 239)',
    'rgb(144, 132, 239)',
    'rgb(195, 132, 239)',
    'rgb(239, 132, 217)'
]
function userMostSentMessage(data) {
    let ctx = document.getElementById('mostDid');
    let userMostSentMessage = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: Object.keys(data),
            datasets: [{
                data: Object.values(data),
                backgroundColor: colours
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Who sent the most messages',
                }
            },
            maintainAspectRatio: false
        }
    });
}

function userSaidName(data) {
    let ctx = document.getElementById('people-graph');
    let userSaidName = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(data),
            datasets: Object.keys(data[Object.keys(data)[0]]).map(function (name, index) {
                return {
                    label: name,
                    data: Object.keys(data).map(function (user) {
                        return data[user][name];
                    }),
                    backgroundColor: colours[index % colours.length] // gets colour based on users modulo
                };
            })
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'User said whos name the most'
                }
            },
            maintainAspectRatio: false
        }
    });
}

function mostUsedWord(data){
    let ctx = document.getElementById('people-graph');
    let mostUsedWord = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: 'Words',
                data: Object.values(data),
                backgroundColor: 'blue'
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'What word was typed the most',
                }
            },
        maintainAspectRatio: false
    }
    })
}

function nameCount(data){
    let ctx = document.getElementById('nameSaid');
    let nameCount = new Chart(ctx, {
        type: 'polarArea',
        data: {
            labels: Object.keys(data),
            datasets: [{
                data: Object.values(data),
                backgroundColor: colours
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top'
                },
                title: {
                    display: true,
                    text: 'Who name was said the most'
                }
            },
            maintainAspectRatio: false
        }
    })
}

function respondedMessage(data){
    let ctx = document.getElementById('stats');
    let respondedMessage = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(data),
            datasets: [{
                label: 'Users',
                data: Object.values(data),
                backgroundColor: colours
            }]
            // datasets: Object.keys(data).map((label, index) => {
            //     return {
            //         label: String(label),
            //         data: Number(data[label]),
            //         backgroundColor: colours[index % colours.length]
            //     };
        },
        options: {
            responsive: true,
            plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Ignored within 10 minutes'
            }
            },
            maintainAspectRatio: false
    }
});
}
