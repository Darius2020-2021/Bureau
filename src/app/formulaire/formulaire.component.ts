import { Component, OnInit } from '@angular/core';
import {NgForm} from "@angular/forms"
@Component({
  selector: 'app-formulaire',
  templateUrl: './formulaire.component.html',
  styleUrls: ['./formulaire.component.scss']
})
export class FormulaireComponent implements OnInit {
  default= "éteint"
  constructor() { }

  ngOnInit(): void {
  }
  onSubmit(form: NgForm){
    console.log(form.value)
  }
}
