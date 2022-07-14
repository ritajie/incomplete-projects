async function request(url, method, data) {
    let response = await fetch(url, {
        method: method,
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    let response_json = await response.json();
    code = response_json.code;
    if (code == 200) {
        return response_json.data;
    }
    else {
        alert(response_json.message);
        return false;
    }
}

async function getBulidings() {
    let response = await request('/api/buildings', 'GET');
    return response;
}
