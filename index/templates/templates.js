export const navtemplate = `
  <colm class="col-md"></colm>
  <colm class="col-md"><h5 onclick="index.content.about()">about me</h5></colm>
  <colm class="col-md"><h5 onclick="index.content.work()">employment</h5></colm>
  <colm class="col-md"><h5 onclick="index.content.school()">education</h5></colm>
  <colm class="col-md"><h5 onclick="index.content.goals()">ambitions</h5></colm>
  <colm class="col-md"><h5 onclick="index.content.expect()">expectations</h5></colm>
  <colm class="col-md"></colm>
  `

export const content = `
  <row class="row">
    <colm class="col-md-3" id="sb-left"></colm>
    <colm class="col-md">
      <row class="row" id="title"></row>
      <row class="row" id="content-text"></row>
    </colm>
    <colm class="visually-hidden col-md-2" id="sb-right"></colm>
  </row>
`

export const profile = `<p></p>`
export const work = `<p></p>`
export const school = `<p></p>`
export const goals = `<p></p>`
export const expect = `<p></p>`