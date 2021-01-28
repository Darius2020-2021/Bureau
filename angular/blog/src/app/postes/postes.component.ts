import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { myPosteService } from '../service/myPoste.service';

@Component({
  selector: 'app-postes',
  templateUrl: './postes.component.html',
  styleUrls: ['./postes.component.scss']
})
export class PostesComponent implements OnInit {
Postes: listPoste[]= []
love(){
  window.alert("vous avez kiffez ce poste")
};
lovent(){
  window.alert("vous n'avez pas kiffez ce poste")
};
heure = new Date();
  constructor(private myPosteService : myPosteService) { }
  
  ngOnInit(): void {
  }

}
