import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-postes',
  templateUrl: './postes.component.html',
  styleUrls: ['./postes.component.scss']
})
export class PostesComponent implements OnInit {
  postes=[{
    title_poste:"Mon premier poste",
    description:"j'apprend a devenir le meilleur devloppeur et j'y arriverais , je rencontrera des tas d'obstacles mais j'abandonnerais pas",
    color:'#9CEF5A'
  },
  {
    title_poste:"Mon seconde poste",
    description:"j'apprend a devenir le meilleur devloppeur et j'y arriverais , je rencontrera des tas d'obstacles mais j'abandonnerais pas",
    color: '#EC7063'
  },
  {
    title_poste:"Mon troisieme poste",
    description:"j'apprend a devenir le meilleur devloppeur et j'y arriverais , je rencontrera des tas d'obstacles mais j'abandonnerais pas",
    color:""
  }
];
love(){
  window.alert("vous avez kiffez ce poste")
};
lovent(){
  window.alert("vous n'avez pas kiffez ce poste")
};
heure = new Date();
  constructor() { }

  ngOnInit(): void {
  }

}