import { expect, goals, profile, school, work } from "./templates/templates.js"

export class ContentController {
  about () {
    document.getElementById( 'title' ).innerHTML = '<h2>profile</h2>'
    document.getElementById( 'content-text' ).innerHTML = profile
  }
  work () {
    document.getElementById( 'title' ).innerHTML = '<h2>employment history</h2>'
    document.getElementById( 'content-text' ).innerHTML = work
  }
  school () {
    document.getElementById( 'title' ).innerHTML = '<h2>education history</h2>'
    document.getElementById( 'content-text' ).innerHTML = school
  }
  goals () {
    document.getElementById( 'title' ).innerHTML = '<h2>ambitions</h2>'
    document.getElementById( 'content-text' ).innerHTML = goals
  }
  expect () {
    document.getElementById( 'title' ).innerHTML = '<h2>expectations</h2>'
    document.getElementById( 'content-text' ).innerHTML = expect
  }
}
