import {Injectable} from '@angular/core';
@Injectable({
  providedIn: 'root',
}
)
export class myPosteService{
 publi =[
    {
    title_poste:"Mon premier poste",
    description:"j'apprend a devenir le meilleur devloppeur et j'y arriverais , je rencontrera des tas d'obstacles mais j'abandonnerais pas",
      },
      {
        title_poste:"Mon seconde poste",
        description:"j'apprend a devenir le meilleur devloppeur et j'y arriverais , je rencontrera des tas d'obstacles mais j'abandonnerais pas",
      },
      {
        title_poste:"Mon dernier poste",
        description:"j'apprend a devenir le meilleur devloppeur et j'y arriverais , je rencontrera des tas d'obstacles mais j'abandonnerais pas",
      }
    ];

    constructor(){}
}
  
