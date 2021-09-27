import { cont, row } from "../style/style.js"
import { Templates } from "./templates.js"

const template = new Templates

function body () {
  document.getElementById( 'body' ).classList.add( cont )
  document.getElementById( 'body' ).innerHTML = template.body
}
function header () {
  document.getElementById( 'header' ).classList.add( cont )
  document.getElementById( 'header' ).innerHTML = template.header
}
function nav () {
  document.getElementById( 'nav' ).classList.add( row )
  document.getElementById( 'nav' ).innerHTML = template.nav
}
function content () {
  document.getElementById( 'main' ).classList.add( row )
  document.getElementById( 'main' ).innerHTML = template.main
}
function footer () {
  document.getElementById( 'footer' ).classList.add( cont )
  document.getElementById( 'footer' ).innerHTML = template.footer
}

export function structure () {
  body()
  header()
  nav()
  content()
  footer()
}