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
  private report = [];
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

  setReport(x:any){
    this.report = x;
  }

  getReport(){
    return this.report;
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

 fetchReport(): Observable<any> {
    this.options = { params: new HttpParams().set('name', "John") };
    return this.http.get<any>('/api/get_attendance_file', this.options);
}

sendAttendance(x:any): Observable<any> {
    this.options = { list: x, name: this.className };
    return this.http.post<any>('/api/update_class', this.options);
}

 fetchNames(): Observable<any> {
    return this.http.get<any>('/api/get_names');
}
}
