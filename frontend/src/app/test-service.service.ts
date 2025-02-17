import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TestServiceService {

  constructor(private http: HttpClient) { }
  private classData = [];
  private nameData = [];
  private className = "";
  options: any;
  setData (x: any){
    this.classData = x;
  }

  getData(){
    return this.classData;
  }

  getNames(){
    return this.nameData;
  }

  setNames(x:any){
    this.nameData = x;
  }

   setClass(x:any){
    this.className = x;
    this.options = { params: new HttpParams().set('name', this.className) };
  }

  getStudentData(){
    return this.classData[0]['students'];
  }
 fetchClassData(): Observable<any> {
    return this.http.get<any>('/api/get_class', this.options);
}

 fetchNames(): Observable<any> {
    return this.http.get<any>('/api/get_names');
}
}
