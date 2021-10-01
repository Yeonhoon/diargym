
import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'

setInteractionMode('eager')

extend('digits', {
  ...digits,
  message: '{_field_} needs to be {length} digits. ({_value_})',
})

extend('required', {
  ...required,
  message: '{_field_}는 필수입력 항목입니다.',
})

extend('max', {
  ...max,
  message: '{_field_} may not be greater than {length} characters',
})

extend('regex', {
  ...regex,
  message: '{_field_} {_value_} does not match {regex}',
})

extend('email', {
  ...email,
  message: '올바른 이메일 형식이 아닙니다.',
})


extend('password', {
  params:['target'],
  validate(value, {target}){
    return value === target;
  },
  message: 'Password Does not Match'
  
})

export default {
    components:{
          ValidationObserver, ValidationProvider,
    },

}