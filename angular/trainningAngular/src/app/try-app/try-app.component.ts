import { Component, Input, OnInit  } from '@angular/core';

@Component({
  selector: 'app-try-app',
  templateUrl: './try-app.component.html',
  styleUrls: ['./try-app.component.scss']
})
export class TryAppComponent implements OnInit {
  
  @Input() listAppareil!:string;
  etatStatus = "éteint";

  constructor() { }

  ngOnInit(): void {
  }
  getStatus(){
    return this.etatStatus;
  }

}
