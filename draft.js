function focusDetails(group, id) {
    let detailsElements = document.getElementsByClassName(group + '-details')
    console.log(detailsElements)
    for (let i = 0; i < detailsElements.length; i++) {
        let element = detailsElements[i]
        let state = element.getAttribute('open')
        element.toggleAttribute('open', !state)
    }
    document.getElementById(id).setAttribute('open') = true
}