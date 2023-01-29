function loadlist() {
    console.log("GOT TO LOADLIST")
    var htmlVAR = '';
    fetch('/list_data/')
    .then(res => res.json())
    .then(data => {
        console.log(data);
        document.getElementById('list-wrapper');
        if (data.error == 'No Tasks') {
            htmlVAR += `no tasks`;
        } else {
            for (let i = 0; i < data.length; i++) {
                console.log(data[i].id, data[i].title);
                addDiv(data[i].title, data[i].id);
            }
        }
        htmlVAR += "</table>";
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

function addDiv(title, id) {
    var newDiv = document.createElement("div");
    newDiv.innerHTML = `
    <div class="list-item pointer-events-auto w-[21rem] rounded-lg bg-white p-4 text-[0.8125rem] leading-5 shadow-xl shadow-black/5 hover:bg-slate-50 ring-1 ring-slate-700/10">
        <div class="flex justify-between">
            <div class="font-medium text-slate-900">
                <a onclick="setScalar(1.0)">${title}</a>
            </div>
        </div>
    </div>`;
    document.body.appendChild(newDiv);
}

function onclick(id) {
    console.log(id);

    // make change on database
    setScalar(0.1);
}

