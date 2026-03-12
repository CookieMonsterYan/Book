# HEBook 国际标准资料清单

> 收录欧美各国水力模型工程师资质要求、技术标准与最佳实践指南

## 一、英国标准 (UK Standards)

### 1. CIWEM Urban Drainage Group (UDG) Competency Framework
**来源：** [CIWEM官网](https://www.ciwem.org/assets/pdf/Special%20Interest%20Groups/Urban%20Drainage%20Group/UDG-Competency-Framework.pdf)

**核心内容：**
- **11个知识领域 (Knowledge Groups)**，共57项具体能力
- **评分体系：** 1-5级评分标准，Level 4 为专业会员资格要求，Level 5 为专家级别
- **核心能力群 (Core Competences)：** 33项被标记为核心能力

**关键知识领域：**
| 知识领域 | 核心能力 |
|---------|---------|
| Legislative Framework and Funding | 立法、法规、资金规划 |
| Stakeholder Engagement | 利益相关者管理、客户关系 |
| Planning, Risk & Serviceability | 下水道风险管理、服务水平 |
| Integrated Urban Drainage | 综合城市排水、水文、SuDS |
| Data Collection and Management | 资产管理、数据采集 |
| **Hydraulic Modelling** | **1D建模、验证、2D建模、风险建模** |
| Feasibility and Catchment Strategy | 可行性评估 |
| Engineering Design and Construction | 设计标准、施工技术 |
| Health, Safety, Environmental | H&S管理、可持续性 |
| Project Management | 项目管理、合同管理 |
| General Skills | 技术软件、GIS、报告撰写 |

**水力建模能力详细分解：**
- 6.1 1D Model Building（一维模型构建）
  - 管网几何与阻力
  - 降雨输入与径流模型
  - 检查、审核与审计
- 6.2 Hydraulic Verification（水力验证）
  - 旱流验证、暴雨事件验证
  - 季节性变化、遥测数据验证
- 6.3 Water Quality Verification（水质验证）
- 6.4 2D Modelling（二维建模）
- 6.5 IUD Modelling（综合城市排水建模）
- 6.6 Risk Modelling（风险建模）
- 6.7 Model Use（模型应用）

**对本书第2章的贡献：**
此框架为构建**L1-L5水力模型团队能力评级体系**提供了国际对标基准。

---

### 2. UK-SPEC (UK Standard for Professional Engineering Competence)
**来源：** [Engineering Council](https://www.engc.org.uk/media/a1yfae02/uk-spec-fourth-edition.pdf)

**核心内容：**
- **CEng (Chartered Engineer)** 能力标准
- 四大能力维度：
  - A: Knowledge and understanding
  - B: Design, development and solving engineering problems
  - C: Technical and commercial leadership
  - D: Professional conduct and ethics

---

## 二、美国标准 (US Standards)

### 1. FEMA Hydraulic Modeling Guidelines
**来源：** [FEMA Floodplain Management](https://www.fema.gov/flood-maps/products-tools/numerical-models)

**核心内容：**
- **认可的软件清单：** HEC-RAS, HEC-HMS, MIKE, TUFLOW 等
- **No-Rise Certification 要求：** 44 CFR Part 60.3(d)(3)
- **模型验证要求：** 必须使用 CHECK-RAS 或 CHECK-2 进行验证
- **建模标准：**
  - 1D/2D 模型选择准则
  - 有效模型 (Effective Model) 必须保持原始格式
  - 校准要求：如有高质量数据必须进行校准

**FEMA 水力模型师职责 (参考职位要求)：**
- 使用 HEC-RAS/HEC-HMS 开发水文水力模型
- 进行洪水频率分析 (Flood Frequency Analysis)
- 准备 CLOMR/LOMR 申请文件
- 确保符合联邦、州和地方的雨水法规

**对本书第4章的贡献：**
FEMA 对模型验证和认证的严格要求，体现了**水力模型架构师 (Hydraulic Modeling Architect)** 角色的必要性。

---

### 2. EPA Architecture and Engineering Guidelines
**来源：** [EPA AE Guidelines](https://www.epa.gov/sites/default/files/2018-03/documents/ae_guidelines_508.pdf)

**核心内容：**
- CFD (Computational Fluid Dynamics) 建模要求
- 风/气流建模标准
- 室外设计条件基于 ASHRAE Handbook

---

## 三、澳大利亚标准 (Australian Standards)

### 1. Australian Rainfall and Runoff (ARR) - 国家权威指南
**来源：** [arr-software.org](https://www.arr-software.org/pdfs/ARR_190514_Book1_V4.2.pdf)

**核心内容：**
- **Book 1:** 指南范围与不确定性分析
- **Book 8:** 极罕见到极端洪水估算
  - 模型选择标准 (Basic vs Enhanced Capabilities)
  - 半分布式 vs 集总式模型
  - 气候变化考量

**不确定性分析框架：**
- 承认设计洪水估算中的固有不确定性
- 区分参数不确定性和模型结构不确定性
- 推荐使用蒙特卡洛方法

**建模能力要求：**
| 能力类型 | 具体要求 |
|---------|---------|
| Basic Requirements | 流域汇流要素表示、降雨空间变异、分布式输出 |
| Enhanced Capabilities | 非线性汇流响应、复杂流域应用 |

---

### 2. Queensland Transport and Main Roads Guidelines
**来源：** [TMR Technical Guidelines](https://www.tmr.qld.gov.au/-/media/busind/techstdpubs/Hydraulics-and-drainage/Hydrologic-and-Hydraulic-Modelling/)

**核心内容：**
- **RPEQ 要求：** 必须由昆士兰州注册专业工程师 (Registered Professional Engineer of Queensland) 认证
- **模型标准：**
  - 优先使用 TUFLOW (2D 水力建模)
  - 也接受 MIKEFLOOD, HEC-RAS 2D
  - 径流-汇流模型：URBS, RORB, WBNM, XP-RAFTS
- **设计事件：** 需评估 50%, 20%, 10%, 5%, 2%, 1%, 0.05% AEP
- **关键持续时间分析：** 必须记录关键持续时间、临界流量、临界时间模式

**对本书第3章的贡献：**
澳大利亚对**注册工程师签字认证**的严格要求，反映了**复合能力**的重要性——既懂水力又懂法规标准。

---

### 3. 地方政府要求示例 (Sutherland Shire Council)
**来源：** [Stormwater Management Specification](https://www.sutherlandshire.nsw.gov.au/)

**核心要求：**
- 所有水文计算必须由 **Chartered Professional Engineer NPER (Civil)** 认证
- 所有水力计算必须由 **Chartered Professional Engineer NPER (Civil)** 认证
- 考虑气候变化对降雨强度和海平面的影响

---

## 四、资料总体分析与本书应用

### 国际趋势总结

| 维度 | 英国 | 美国 | 澳大利亚 |
|------|------|------|----------|
| **能力认证** | CIWEM C.WEM | PE License | RPEQ / CPEng |
| **建模标准** | UDG Framework | FEMA Guidelines | ARR Guidelines |
| **验证要求** | 内部审核体系 | CHECK-RAS强制验证 | 关键持续时间分析 |
| **签字权** | 特许工程师 | 注册工程师 | 州注册工程师 |
| **质量控制** | 公司级QA体系 | FEMA审查 | 政府技术审查 |

### 对本书各章节的贡献

**第1章 - 团队重要性：**
- 各国标准都强调模型质量直接影响公共安全
- FEMA 将模型认证与保险费率挂钩

**第2章 - 能力评级：**
- CIWEM UDG 框架提供 1-5 级评分体系模板
- 澳大利亚 ARR 提供模型复杂度分级标准

**第3章 - 团队建设：**
- 复合能力是国际通行要求（水力+法规+软件）
- 持续专业发展 (CPD) 是维持资质的必要条件

**第4章 - 团队结构：**
- 审核/验证角色独立于建模角色（质量保证）
- 注册工程师承担最终签字责任

**第5章 - AI 应用：**
- 不确定性分析框架为 AI 辅助决策提供理论基础
- 自动化验证工具 (CHECK-RAS) 是 AI 应用的先例

---

## 五、下一步工作

1. **深度翻译：** 对 CIWEM UDG Framework 进行全文翻译
2. **案例收集：** 收集各国标准在实际项目中的应用案例
3. **对比分析：** 形成中外水力模型工程师能力要求对比表
4. **本土适配：** 将国际标准适配到中国水务行业语境

---
*资料整理时间：2026-03-12*
*整理者：HEBook Research Team*
