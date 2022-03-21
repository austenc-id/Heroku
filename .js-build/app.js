let path = 'assets/data/'
let skills = []
let languages = []
fetch(path + 'headers.json')
    .then(
        headers => {
            return headers.json();
        }
    )
    .then(
        headers => {
            // console.log(headers)
            document.getElementById('main-header').innerHTML = headers.main.text
            document.getElementById('sub-header').innerHTML = headers.sub.text
        }
    )
fetch(path + 'links.json')
    .then(
        links => {
            return links.json();
        }
    )
    .then(
        links => {
            // console.log(links)
            links.forEach(
                link =>
                    document.getElementById('navigation').innerHTML
                    += `<a target="_blank" href="${link.url}">${link.text}</a>`
            );

        }
    )
fetch(path + 'sections.json')
    .then(
        sections => {
            return sections.json();
        }
    )
    .then(
        sections => {
            // console.log(sections)
            sections.forEach(
                section =>
                    document.getElementById('sections').innerHTML
                    += `<details id=${section}-entries>
                            <summary class="text-capitalize">
                                <h3>${section}</h3>
                            </summary>
                        </details>`
            );

        }
    )

fetch(path + 'employment.json')
    .then(
        entries => {
            return entries.json();
        }
    )
    .then(
        entries => {
            // console.log(entries)
            entries.forEach(
                entry => {
                    document.getElementById('employment-entries').innerHTML
                        += `<details id=${entry.position}-entry>
                                <summary>
                                    <h6>${entry.position}</h6>
                                </summary>
                                <strong>${entry.org}</strong>
                                <br>
                                <small><i>${entry.dates.start} - ${entry.dates.end}</i></small>
                            </details>`
                    entry.skills.forEach(
                        skill => {
                            if (!skills.includes(skill)) {
                                skills.push(skill)
                                document.getElementById('skills-entries').innerHTML
                                    += `<li>${skill}</li>`
                            }
                        }
                    )
                    entry.languages.forEach(
                        language => {
                            if (!languages.includes(language)) {
                                languages.push(language)
                                document.getElementById('programming-languages/frameworks-entries').innerHTML
                                    += `<li>${language}</li>`
                            }
                        }
                    )
                }
            )
        }
    )

fetch(path + 'education.json')
    .then(
        entries => {
            return entries.json();
        }
    )
    .then(
        entries => {
            // console.log(entries)
            entries.forEach(
                entry => {
                    document.getElementById('education-entries').innerHTML
                        += `<details id=${entry.program}-entry>
                            <summary>
                                <h6>${entry.program}</h6>
                            </summary>
                            <strong>${entry.org}</strong>
                            <br>
                            <small><i>${entry.dates.start} - ${entry.dates.end}</i></small>
                        </details>`
                    if (entry.completed === true) {
                        // console.log(entry.certificates)
                        entry.certificates.forEach(
                            certification =>
                                document.getElementById('certifications-entries').innerHTML
                                += `<details id=${certification.name}-entry>
                                            <summary>
                                                <h6>${certification.name}</h6>
                                            </summary>
                                            <strong>${certification.org}</strong>
                                            <br>
                                            <small><i>${certification.date}</i></small>
                                        </details>`
                        )
                    }
                    entry.skills.sort()
                    entry.skills.forEach(
                        skill => {
                            if (!skills.includes(skill)) {
                                skills.push(skill)
                                document.getElementById('skills-entries').innerHTML
                                    += `<li>${skill}</li>`
                            }
                        }
                    )
                    entry.languages.forEach(
                        language => {
                            if (!languages.includes(language)) {
                                languages.push(language)
                                document.getElementById('programming-languages/frameworks-entries').innerHTML
                                    += `<li>${language}</li>`
                            }
                        }
                    )
                }
            )
        }
    )
