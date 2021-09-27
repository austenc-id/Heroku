import { Left, Right } from "./content/Sidebars.js"
import { ContentController } from "./ContentController.js"
import { content, navtemplate } from "./templates/templates.js"

class Index {
  left = new Left
  right = new Right
  content = new ContentController
  home () {
    document.getElementById( 'body' ).innerHTML = 'GOODBYE'
    document.getElementById( 'body' ).classList.toggle( 'text-center' )
  }
  initialize () {
    document.getElementById( 'navigation' ).innerHTML = navtemplate
    document.getElementById( 'content' ).innerHTML = content
    document.getElementById( 'sb-left' ).innerHTML = this.left.bio
    document.getElementById( 'sb-right' ).innerHTML = this.right.links
  }

}

window[ 'index' ] = new Index