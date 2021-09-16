<template>
  <div style="margin-top:50px;">
    <div class="header">
      <h1>Vagas para Pessoas Desenvolvedoras do <b-link href="https://pluo.jobs/" target="_blank"><img alt="Pluo Jobs" class="nav-logo" src="../../assets/pluo-logo-full.png"></b-link></h1>
    </div>
    
    <vue-horizontal responsive>
      <b-card-group deck v-for="item in items" :key="item.i">
        <b-card  bg-variant="dark" text-variant="white" :header="'Job '+(parseInt(item.i)+1)" class="text-center">
          <b-card-text>🚀 {{ item.title }}</b-card-text>
          <b-card-text title="Nome da Organização">💼 {{ item.company_name }}</b-card-text>
          <b-card-text v-if="item.remote == true" title="Aceita trabalho remoto">✅ Remoto</b-card-text> 
          <b-card-text v-else title="Não aceita trabalho remoto">❌ Remoto</b-card-text> 
          <b-button v-b-modal.modal-tall @click="sendInfo(item)" user="'item'">DETALHES</b-button>
        </b-card>
      </b-card-group>
    </vue-horizontal>
    <b-modal id="modal-tall"  size="xl" title="Info Job" centered>
      <div v-if="selectedJob.workplace">
        <h2 class="header">Ambiente de Trabalho</h2>
        <p><span v-html="selectedJob.workplace"></span></p>
      </div>
      <div v-if="selectedJob.description">
        <h2 class="header">Descrição</h2>
        <p><span v-html="selectedJob.description"></span></p>
      </div>
      <div v-if="selectedJob.requirements">
        <h2 class="header">Requerimentos</h2>
        <p><span v-html="selectedJob.requirements"></span></p>  
      </div>        
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'

const pyjobys = axios.create({
    baseURL: 'https://pyjobs.com.br/api',
    timeout: 9000,
})

export default {
  name: 'PyJobCard',
  data() {
      return {
        items: [
          {
            title: '',
            company_name:  '', 
            workplace: '',
            description: '',
            requirements: '',
            remote: '',
            created_at: '',
          },
          {
            title: '',
            company_name:  '', 
            workplace: '',
            description: '',
            requirements: '',
            remote: '',
            created_at: '',
          },
          {
            title: '',
            company_name:  '', 
            workplace: '',
            description: '',
            requirements: '',
            remote: '',
            created_at: '',
          },
          {
            title: '',
            company_name:  '', 
            workplace: '',
            description: '',
            requirements: '',
            remote: '',
            created_at: '',
          },
          {
            title: '',
            company_name:  '', 
            workplace: '',
            description: '',
            requirements: '',
            remote: '',
            created_at: '',
          },
          {
            title: '',
            company_name:  '', 
            workplace: '',
            description: '',
            requirements: '',
            remote: '',
            created_at: '',
          }
        ],
        selectedJob: '',
      }
  },
  mounted () {
    pyjobys.get('/jobs/')
      .then(response =>{
        let i = 0;
        for (i; i < response.data.objects.length;) {
          //i: i
          if(i < 6){
            this.items[i].i = i
            this.items[i].title = response.data.objects[i].title,
            this.items[i].company_name = response.data.objects[i].company_name,
            this.items[i].workplace = response.data.objects[i].workplace,
            this.items[i].description = response.data.objects[i].description,
            this.items[i].requirements = response.data.objects[i].requirements,
            this.items[i].remote = response.data.objects[i].remote,
            this.items[i].created_at = response.data.objects[i].created_at
          }else{
            this.items.push({
            i: i,
            title: response.data.objects[i].title, 
            company_name: response.data.objects[i].company_name, 
            workplace: response.data.objects[i].workplace,
            description: response.data.objects[i].description,
            requirements: response.data.objects[i].requirements,
            remote:  response.data.objects[i].remote,
            created_at: new Date(response.data.objects[i].created_at),
            })
          }
          i++
        } 
      })
      .catch(err=>{
        console.log(err)
      })
  },
  methods:{
    sendInfo(item) {
      this.selectedJob = item;
    },
    getJobs(){
      console.log('Jobs')
    }
  }
}
</script>

<style>
.header{
  text-align: center;
}
</style>