class Position {
    constructor(data) {
        this.Title = data.Title
        this.employer = data.employer
        this.link = data.link
        this.location = data.location
        this.address = this.location.address
        this.city = this.location.city
        this.state = this.location.state
        this.start = formatDate(data.dates.start)
        this.end = formatDate(data.dates.end)
    }
    getTemplate() {
        return `
        <details class="text-capitalize me-1">
            <summary>${this.Title}</summary>
            <li class="border-top border-start border-end">
            <a href="${this.link}" target="_blank">${this.employer}</a>
            </li>
            <li class="border-start border-end">${this.city}, ${this.state}</li>
            <li class="i border-start border-end border-bottom">${this.start} - ${this.end}</li>
        </details>
        `
    }
}
class Program {
    constructor(data) {
        this.Title = data.Title
        this.start = formatDate(data.dates.start)
        this.end = formatDate(data.dates.end)
        this.provider = data.provider
        this.link = data.link
        this.location = data.location
        this.address = this.location.address
        this.city = this.location.city
        this.state = this.location.state
        this.certificate = data.certificate
        if (this.certificate.graduated) {
            this.hidden = ''
        }
        else {
            this.hidden = 'visually-hidden'
        }
    }
    getTemplate() {
        return `
        <details class="text-capitalize me-2">
            <summary>${this.Title}</summary>
            <li class="border-top border-start border-end">
                <a href="${this.link}" target="_blank">${this.provider}</a>
            </li>
            <li class="border-start border-end ${this.hidden}">${this.certificate.Title}</li>
            <li class="border-start border-end">${this.city}, ${this.state}</li>
            <li class="border-start border-end border-bottom">${this.start} - ${this.end}</li>
        </details>
        `
    }
}
function render(section, label) {
    let path = `static/journal/${section}/${label}.json`
    console.log(path)
    fetch(path)
        .then(file => { return file.json() })
        .then(entry => {
            document.getElementById('entry-title').innerHTML = label;
            document.getElementById('entry-content').innerHTML = ''
            entry.story.forEach(paragraph => {
                document.getElementById('entry-content').innerHTML
                    += `<p>${paragraph}</p>`
            });
            if (section === 'employment') {
                let dates = formatDates(entry.dates)
                document.getElementById('entry-dates').innerHTML = dates
                let positions = entry.positions
                document.getElementById('entry-lists').innerHTML
                    = `
                        <section id="positions">
                        <h5>Positions</h5>
                        </section>
                        `

                for (let i = 0; i < positions.length; i++) {
                    let position = positions[i];
                    position = new Position(position)
                    document.getElementById('positions').innerHTML
                        += position.getTemplate()
                }
            }
            if (section === 'education') {
                let programs = entry.programs
                document.getElementById('entry-lists').innerHTML
                    = `
                    <section id="programs">
                    <h5>Programs</h5>
                    </section>
                    `
                for (let i = 0; i < programs.length; i++) {
                    let program = programs[i];
                    program = new Program(program)
                    document.getElementById('programs').innerHTML
                        += program.getTemplate()
                }
            }
            if (section === 'skills') {
                let skills = entry.skills
                document.getElementById('entry-lists').innerHTML
                    = `
                <section id="skills" class="text-capitalize">

                </section>
                `
                let cats = entry.cats
                for (let i = 0; i < cats.length; i++) {
                    let cat = cats[i];
                    document.getElementById('skills').innerHTML
                        += `<h5>${cat}</h5>
                            <section id="${cat}" class="border mb-3"></li>`
                }
                for (let i = 0; i < skills.length; i++) {
                    let skill = skills[i];
                    document.getElementById(`${skill.cat}`).innerHTML
                        += `<li>${skill.label}</li>`
                }
            }
        }
        )
    // .catch(error => console.log(error))
}
function formatDates(dates, format = 'semi-long') {
    let start = formatDate(dates.start, format = format)
    let end = formatDate(dates.end, format = format)
    return `${start} - ${end}`
}
function formatDate(date, format = 'semi-long') {
    let month = date.month
    let day = date.day
    let year = date.year
    if (format === 'semi-long') {
        month = month.substring(0, 3) + '.'
        // year = year.substring(2, 2)
    }
    return `${month} ${day}, ${year}`
}
