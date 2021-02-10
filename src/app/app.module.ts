import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule} from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TryAppComponent } from './try-app/try-app.component';
import { FormulaireComponent } from './formulaire/formulaire.component';
import { SuiteComponent } from './suite/suite.component';

@NgModule({
  declarations: [
    AppComponent,
    TryAppComponent,
    FormulaireComponent,
    SuiteComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
