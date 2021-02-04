import { Component,Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { myPosteService } from '../service/myPoste.service';

@Component({
  selector: 'app-postes',
  templateUrl: './postes.component.html',
  styleUrls: ['./postes.component.scss']
})
export class PostesComponent implements OnInit {
  publis! : any[]
  
@Input() item = String 
 
love(){
  window.alert("vous avez kiffez ce poste")
};
lovent(){
  window.alert("vous n'avez pas kiffez ce poste")
};
heure = new Date();
  constructor(private myPosteService : myPosteService) { }
  

ngOnInit(){
  this.publis = this.myPosteService.publi
}
}
