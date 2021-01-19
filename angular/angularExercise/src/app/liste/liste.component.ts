import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-liste',
  templateUrl: './liste.component.html',
  styleUrls: ['./liste.component.scss']
})
export class ListeComponent implements OnInit {

  Iphone =[{

    produit:"iphone1" },
  {

  produit:" iphone2" },
  {

  produit:"iphone3" },
      {

        produit:" iphone4 " },
        {

          produit:" iphone5" },
          {

            produit:"iphone6" },
            {

              produit:"iphone7 " },
              {

                produit:"iphone8" },
              ];    
 
  iphone=[
    {description:"l'iphone 1 est sorti en 2007 "},
  {
    description:"l'iphone 2 est sorti en 2008 "
  },
  {
    description:"l'iphone 3 est sorti en 2009"
  },
  {
    description:"l'iphone 4 est sorti en 2010"
  },
  {
    description:"l'iphone 5 est sorti en 2011 "
  },
  {
    description:"l'iphone 6 est sorti en 2012"
  },
  {
    description:"l'iphone 7 est sorti en 2013"
  },
  {
    description:"l'iphone 8 est sorti en 20014 "
  },
  ];
  constructor() { }

  ngOnInit(): void {
  }

}
