import { Templates } from "./templates.js"

const templates = new Templates

export class Structure {
  body () {
    document.getElementById( 'body' ).classList.add( 'body', 'container' )
    document.getElementById( 'body' ).innerHTML = templates.body
  }
  top () {
    document.getElementById( 'header' ).classList.add( 'row' )
    document.getElementById( 'header' ).innerHTML = templates.header
    document.getElementById( 'nav' ).classList.add( 'row' )
    document.getElementById( 'nav' ).innerHTML = templates.nav
  }
  bottom () {
    document.getElementById( 'main' ).classList.add( 'row' )
    document.getElementById( 'main' ).innerHTML = templates.main
    document.getElementById( 'footer' ).classList.add( 'container' )
    document.getElementById( 'footer' ).innerHTML = templates.footer
  }
}
