import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TestServiceService {

  constructor(private http: HttpClient) { }
  private classData = [];
  setData (x: any){
    this.classData = x;
  }

  getData(){
    return this.classData;
  }

  getStudentData(){
    return this.classData[0]['students'];
  }
  options = { params: new HttpParams().set('name', "12dfercMa1") };
 fetchClassData(): Observable<any> {
    return this.http.get<any>('/api/get_class', this.options);
}
}
