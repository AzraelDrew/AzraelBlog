import{d as y,b as A,J as E,u as I,a as B,i as c,j as U,r as f,o as F,k as S,l as T,f as m,L as h,M as b,g as s,T as D,E as J,_ as N}from"./index-734f478a.js";import{T as g}from"./TheButton-6961f5fb.js";const j={class:"container editArticle"},M={class:"flex flexJustifySpaceBetween"},R={class:"flex flexJustifyEnd cancelPost"},q=y({__name:"EditArticle",setup(G){const v=A(),o=E(),_=I(),r=B(),l=c(""),n=c(""),i=c(""),d=c(!1);function x(){d.value=!d.value}function V(t,e,u){let p=u[0],a=new FormData;a.append("imgnode",p),r.post("api/article/img/",a).then(C=>{e({url:C.data.url,desc:"在这里插入图片描述"})})}U(async()=>{let e=(await r({url:"api/article/?id="+o.params.id+"&userId="+_.userInfo.id,method:"GET"})).data;n.value=e.title,l.value=e.content,i.value=e.ddescribe});function w(){v.push({name:"ViewArticle",params:{id:o.params.id}})}async function k(){let t=new FormData;t.append("articleId",o.params.id),t.append("token",_.userInfo.token),t.append("title",n.value),t.append("describe",i.value),t.append("content",l.value),t.append("content",l.value);let e=await r.post("api/upadte/article/",t);console.log(e),J({title:"Success",message:"修改成功",type:"success"}),v.push({name:"ViewArticle",params:{id:o.params.id}})}return(t,e)=>{const u=f("el-input"),p=f("v-md-editor");return F(),S(D,{name:"fade",appear:""},{default:T(()=>[m("div",j,[h(m("div",M,[s(u,{modelValue:n.value,"onUpdate:modelValue":e[0]||(e[0]=a=>n.value=a),class:"input",placeholder:"标题..."},null,8,["modelValue"]),s(u,{modelValue:i.value,"onUpdate:modelValue":e[1]||(e[1]=a=>i.value=a),class:"input",placeholder:"描述..."},null,8,["modelValue"])],512),[[b,!d.value]]),s(p,{class:"md","left-toolbar":"undo redo clear | h bold italic strikethrough quote | emoji todo-list | ul ol table hr | link image code | save",modelValue:l.value,"onUpdate:modelValue":e[2]||(e[2]=a=>l.value=a),height:"76vh",onFullscreenChange:x,"disabled-menus":[],onUploadImage:V},null,8,["modelValue"]),h(m("div",R,[s(g,{text:"取消",onClick:w,class:"button cancelButton"}),s(g,{text:"发布",onClick:k,class:"button"})],512),[[b,!d.value]])])]),_:1})}}});const z=N(q,[["__scopeId","data-v-4b1cbf4a"]]);export{z as default};
