<template>
    <div id="loginbody">
        <el-form v-model="ruleForm" status-icon :rules="rules">
            <!-- 用户名 -->
            <el-form-item>
                <el-input v-model="ruleForm.user" prefix-icon="el-icon-user" placeholder="用户名" autocomplete="off"></el-input>
            </el-form-item>
            <!-- 密码 -->
            <el-form-item>
                <el-input tpye="password" v-model="ruleForm.password" prefix-icon="el-icon-lock" placeholder="密码" autocomplete="off"></el-input>
            </el-form-item>
            <!-- 登录按钮 -->
            <el-form-item>
                <el-button type="primary" @click.enter="submitFrom()">登&nbsp;录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    date() { //页面初数据
        return {
            ruleForm: { //存储用户输入数据
                user: '',
                password: '',
            },
            rules: { // 可添加一些表单规则
            }
        }
    },
    methods: {
        submitFrom() {
            this.axios.post('url',{...this.ruleForm}).then(res => { // post请求，携带参数为展开运算符=user: '', passwd: '',
                if(res.code != 0) return false; // 后台根据前端传来的数据返回对应的状态码， 0为成功，继续继续往下执行，非0即失败（-1为用户名或者密码错误，1为空）停止往下执行
                this.$message({ //提示成功信息
                    type: 'success',
                    $message: '登录成功'
                })
                this.$router.push('/home/index') // 成功跳转到首页
            })
        }
    }
}
</script>
