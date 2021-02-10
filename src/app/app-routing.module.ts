import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { FormulaireComponent } from './formulaire/formulaire.component';
import { SuiteComponent } from './suite/suite.component';

const routes: Routes = [
  {path:"suivant", component:SuiteComponent},
  {path:"formule", component: FormulaireComponent},
  {path:"", component:AppComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
