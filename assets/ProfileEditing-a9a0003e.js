import{d as V,a as b,u as I,b as y,D as C,w as N,r as c,o as w,c as U,g as e,l as o,h as T,R as A,f as u,x as m,T as D,F as E,_ as P}from"./index-12433a3f.js";import{a as B,b as L,T as S}from"./TheNavBar-29ea6621.js";const z={class:"profileEditing flex"},F={class:"flex flexDirectionColumn box"},R={class:"flex flexJustifyStart changeAvatar"},G={class:"form"},J=V({__name:"ProfileEditing",setup(j){const f=b(),n=I(),i=y(),a=C({name:n.userInfo.username,nickName:n.userInfo.name,avatar:n.userInfo.avatar,phone:n.userInfo.phone,desc:n.userInfo.desc});async function _(l){console.log(l),a.avatar="",a.avatar=l.url}N(n.userInfo,async()=>{n.GetUserInfo(n.userInfo.token)});async function v(){console.log("submit!");let l=new FormData;l.append("token",n.userInfo.token),l.append("name",a.name),l.append("nickName",a.nickName),l.append("avatar",a.avatar),l.append("phone",a.phone),l.append("desc",a.desc),await f.post("api/update/userinfo/",l),n.GetUserInfo(n.userInfo.token),i.replace({name:"Profile"})}function x(){console.log("cancel!"),i.replace({name:"Profile"})}function k(){n.userLogout(),i.replace({name:"Login"})}return(l,t)=>{const p=c("el-button"),h=c("el-upload"),d=c("el-input"),r=c("el-form-item"),g=c("el-form");return w(),U(E,null,[e(L,null,{avatarAndNickname:o(()=>[e(T(A),{to:"/",class:"link",href:""},{default:o(()=>[e(B,{class:"home icon",icon:"iconzhuye3",size:30})]),_:1})]),dropDown:o(()=>[u("div",null,[u("a",{onClick:k,class:"link linkColor"},"退出登录")])]),_:1}),e(D,{name:"fade",appear:""},{default:o(()=>[u("div",z,[u("div",F,[u("div",R,[e(S,{size:50,src:a.avatar},null,8,["src"]),e(h,{class:"upload-demo flex",multiple:"",limit:3,name:"avatar",action:"http://43.138.126.114:8000/api/upload/avatar/","on-success":_},{default:o(()=>[e(p,{class:"uploadAvatar",round:""},{default:o(()=>[m("修改头像")]),_:1})]),_:1})]),u("div",G,[e(g,{model:a,"label-width":"120px"},{default:o(()=>[e(r,{class:"flex",label:"用户名:"},{default:o(()=>[e(d,{class:"input",modelValue:a.name,"onUpdate:modelValue":t[0]||(t[0]=s=>a.name=s)},null,8,["modelValue"])]),_:1}),e(r,{class:"flex",label:"昵称:"},{default:o(()=>[e(d,{class:"input",modelValue:a.nickName,"onUpdate:modelValue":t[1]||(t[1]=s=>a.nickName=s)},null,8,["modelValue"])]),_:1}),e(r,{class:"flex",label:"电话:"},{default:o(()=>[e(d,{class:"input",modelValue:a.phone,"onUpdate:modelValue":t[2]||(t[2]=s=>a.phone=s)},null,8,["modelValue"])]),_:1}),e(r,{class:"flex",label:"简介:"},{default:o(()=>[e(d,{class:"input",type:"textarea",rows:8,modelValue:a.desc,"onUpdate:modelValue":t[3]||(t[3]=s=>a.desc=s),maxlength:200},null,8,["modelValue"])]),_:1}),e(r,{class:"button"},{default:o(()=>[e(p,{type:"primary",onClick:v},{default:o(()=>[m("Submit")]),_:1}),e(p,{onClick:x},{default:o(()=>[m("Cancel")]),_:1})]),_:1})]),_:1},8,["model"])])])])]),_:1})],64)}}});const K=P(J,[["__scopeId","data-v-dec148de"]]);export{K as default};
