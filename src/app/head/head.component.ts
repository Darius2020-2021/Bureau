import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-head',
  templateUrl: './head.component.html',
  styleUrls: ['./head.component.scss']
})
export class HeadComponent implements OnInit {
iconConnect : String="assets/images/connectionVrai2.png"
  constructor() { }

  ngOnInit(): void {
  }

}
