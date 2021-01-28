import { Component,Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { myPosteService } from '../service/myPoste.service';

@Component({
  selector: 'app-postes',
  templateUrl: './postes.component.html',
  styleUrls: ['./postes.component.scss']
})
export class PostesComponent implements OnInit {
  postes: publi[] = []
  
@Input() item = String 
  publi: any[];
love(){
  window.alert("vous avez kiffez ce poste")
};
lovent(){
  window.alert("vous n'avez pas kiffez ce poste")
};
heure = new Date();
  constructor(private myPosteService : myPosteService) { }
  
  getPostes(): void {
    this.publi = this.myPosteService.getPostes();
  }
ngOnInit(){
  this.getPostes
}
}
