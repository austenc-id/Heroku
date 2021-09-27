import { Structure } from "./structure.js"
const structure = new Structure
class Index {

  initialize () {
    structure.body()
    structure.top()
    structure.bottom()
  }
}

window[ 'index' ] = new Index