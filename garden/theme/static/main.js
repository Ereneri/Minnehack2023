function loadlist() {
    console.log("GOT TO LOADLIST")
    var htmlVAR = "<ul>";
    fetch('/list_data/')
    .then(res => res.json())
    .then(data => {
        console.log(data);
        document.getElementById('list-wrapper');
        if (data.error == 'No Tasks') {
            htmlVAR += `<h2 id="notasks" style="text-align: center; margin-top: 2rem">No Tasks...</h2>`;
        } else {
            for (let i = 0; i < data.length; i++) {
                console.log(data[i].id, data[i].title);
                htmlVAR += `<li class="list-item" id="list-item-${data[i].id}"><span class="list-item-title">${data[i].title}</span>`;
            }
        }
        htmlVAR += "</ul>";
        document.getElementById('list-wrapper').innerHTML += htmlVAR;
    })
    console.log("FINISHED LOADLIST")
}

function completeTask(id) {
    console.log(id + boolean);
    var user = JSON.parse(document.getElementById('requestuser').textContent);

    // make change on database
    fetch('/completetask/' + id, {
        method: 'PUT',
        body: JSON.stringify({
            iscomplete: boolean
        })
    })
}