export class Left {
  constructor () {
    this.image = 'assets/images/bio.jpg'
    this.biography = 'Hello, I am me.'
  }
  get bio () {
    return `
      <container class="container-flex">
        <row class="row">
          <img src="${this.image}" alt="profile-image">
        </row>
        <row class="row">
          <p id="">${this.biography}</p>
        </row>
      </container>
    `
  }
}
export class Right {
  constructor () {
  }
  get links () {
    return `
    `
  }
}