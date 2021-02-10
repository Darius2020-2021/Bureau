import {Injectable} from '@angular/core'
@Injectable({
    providedIn:'root'
})

export class ComponentService{
    const appareilObject={
        id:0,
        name:'',
        status:''
    };
    appareilObject.name= name;
    appareilObject.status=status;
    appareilObject.id=this.appareils[(this.appareilObject.length-1)].id+1;
}