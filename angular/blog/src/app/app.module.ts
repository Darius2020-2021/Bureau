import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PostesComponent } from './postes/postes.component';
import { ProfilComponent } from './profil/profil.component';
import { myPosteService } from './service/myPoste.service';

@NgModule({
  declarations: [
    AppComponent,
    PostesComponent,
    ProfilComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [myPosteService],
  bootstrap: [AppComponent]
})
export class AppModule { }
