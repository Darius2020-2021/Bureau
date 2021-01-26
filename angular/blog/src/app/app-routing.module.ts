import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PostesComponent } from './postes/postes.component';
import { ProfilComponent } from './profil/profil.component';

const routes: Routes = [
  {path: '', component: PostesComponent},
  {path:'profile', component: ProfilComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
