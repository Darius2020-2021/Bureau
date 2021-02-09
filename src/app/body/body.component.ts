import { Component, OnInit } from '@angular/core';
import * as AOS from 'aos';
@Component({
  selector: 'app-body',
  templateUrl: './body.component.html',
  styleUrls: ['./body.component.scss']
})
export class BodyComponent implements OnInit {
  vendre: String="assets/images/vendreVrai.jpg"
  constructor() { }

  ngOnInit(): void {
    AOS.init({
      duration: 1200,
    })
  }

}
