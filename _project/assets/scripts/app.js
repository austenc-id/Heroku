function show(target) {
    let entries = document.getElementsByClassName('entries')
    for (let i = 0; i < entries.length; i++) {
        let entry = entries[i]
        console.log(entry)
        entry.classList.add('visually-hidden')
    }
    document.getElementById(target).classList.remove('visually-hidden')
    document.getElementById(target).classList.add('active')
    console.log()
}