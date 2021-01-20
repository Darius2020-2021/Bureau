import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-liste',
  templateUrl: './liste.component.html',
  styleUrls: ['./liste.component.scss']
})
export class ListeComponent implements OnInit {

  Iphones =[{

    produit:"iphone1" ,
    description : "l'iphone 1 est sorti en 2007 " },
  {

  produit:" iphone2" ,
  description:"l'iphone 2 est sorti en 2008 "
},
  {

  produit:"iphone3" ,
  description:"l'iphone 3 est sorti en 2009"
},
{
produit:" iphone4 " ,
description:"l'iphone 4 est sorti en 2010"
},
{

produit:" iphone5" ,
description:"l'iphone 5 est sorti en 2011 "
},
{
produit:"iphone6" ,
description:"l'iphone 6 est sorti en 2012"
},
{
produit:"iphone7 " ,
description:"l'iphone 7 est sorti en 2013"
},
{
produit:"iphone8",
description:"l'iphone 8 est sorti en 20014 "
},
];                 
achat(){
  window.alert("l'achat a été écffectué");
  }
precomander(){
  window.alert("votre produits a été précommander")
}
 
  constructor() { }

  ngOnInit(): void {
  }

}
