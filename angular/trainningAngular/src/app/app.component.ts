import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  auto = false;
  machine1="TV";
  machine2="iphone";
  machine3="samsung";
  constructor(){
    setTimeout(
      () =>{
        this.auto=true
      }, 5000
    )
  }
  onAllume(){
    console.log('on allume tout')
  }
   }

