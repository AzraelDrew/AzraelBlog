import{d as b,b as V,u as g,a as k,i as d,r as c,o as w,k as B,l as C,f as u,g as a,T,_ as y}from"./index-12433a3f.js";import{T as p}from"./TheButton-a372b650.js";const P={class:"container"},A={class:"flex flexJustifySpaceBetween"},S={class:"flex flexJustifyEnd cancelPost"},U=b({__name:"PostArticle",setup(E){const m=`::: tip
  你可以点击 toolbar 中的 tip 来快速插入
:::

::: warning
  这是一段警告
:::

::: danger
  这是一个危险警告
:::

::: details
  这是一个详情块，在 IE / Edge 中不生效
:::

::: tip 自定义标题
  你也可以自定义块中的标题
:::

::: danger STOP
  危险区域，禁止通行
:::

`,i=V(),_=g(),f=k(),l=d(m),s=d(""),n=d("");function v(){i.push({name:"Home"})}async function x(){let t=new FormData;t.append("token",_.userInfo.token),t.append("title",s.value),t.append("describe",n.value),t.append("content",l.value),t.append("cover","");let e=await f.post("api/add/article/",t);console.log(e),i.push({name:"Home"})}return(t,e)=>{const r=c("el-input"),h=c("v-md-editor");return w(),B(T,{name:"fade",appear:""},{default:C(()=>[u("div",P,[u("div",A,[a(r,{modelValue:s.value,"onUpdate:modelValue":e[0]||(e[0]=o=>s.value=o),class:"input",placeholder:"标题..."},null,8,["modelValue"]),a(r,{modelValue:n.value,"onUpdate:modelValue":e[1]||(e[1]=o=>n.value=o),class:"input",placeholder:"描述..."},null,8,["modelValue"])]),a(h,{class:"md","left-toolbar":"undo redo clear | h bold italic strikethrough quote | emoji todo-list | ul ol table hr | link image code | save",modelValue:l.value,"onUpdate:modelValue":e[2]||(e[2]=o=>l.value=o),autofocus:!0,height:"70vh"},null,8,["modelValue"]),u("div",S,[a(p,{text:"取消",onClick:v,class:"button cancelButton"}),a(p,{text:"发布",onClick:x,class:"button"})])])]),_:1})}}});const H=y(U,[["__scopeId","data-v-302b57f6"]]);export{H as default};
